import click
from gql import Client, gql

from apyb import config
from apyb.email import send_email_as_no_reply
from apyb.github.client import get_github_client
from apyb.templates import render_template


def get_discussion(github: Client, discussion_id: int):
    query = """{{
        repository(owner: "{owner}", name: "{name}") {{
            discussion(number: {discussion}) {{
                title
                url
                bodyHTML
            }}
        }}
    }}
    """.format(
        owner=config.APYB_GITHUB_ORG,
        name=config.APYB_GITHUB_COMMUNITY_REPO,
        discussion=discussion_id,
    )
    response = github.execute(gql(query))
    return response["repository"]["discussion"]


@click.command("github:new-discussion-notification")
@click.option(
    "--no-reply-password",
    required=True,
    envvar="APYB_BOT_NO_REPLY_PASSWORD",
    help="Password for the noreply@ email",
)
@click.option(
    "--token", required=True, envvar="APYB_BOT_GITHUB_TOKEN", help="GitHub API token"
)
@click.option(
    "--send-to", required=True, envvar="APYB_BOT_SEND_TO", help="Discussion ID number"
)
@click.option("--id", type=int, required=True, help="Discussion ID number")
def new_discussion_notification(
    id: int,
    send_to: str,
    token: str,
    no_reply_password: str,
):
    github = get_github_client(token)
    discussion = get_discussion(github, id)

    email_subject = discussion["title"]
    email_body = render_template(
        "email_new_discussion.html",
        title=discussion["title"],
        url=discussion["url"],
        body=discussion["bodyHTML"],
    )
    send_email_as_no_reply(send_to, email_subject, email_body, no_reply_password)
