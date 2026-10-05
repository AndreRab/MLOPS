import os
import argparse
from dotenv import load_dotenv
from settings import Settings
import yaml
import subprocess


def export_envs(environment: str = "dev") -> None:
    load_dotenv(f"config/.{environment}.env")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)

    result = subprocess.run(
        ["sops", "--decrypt", "secrets.yaml"],
        capture_output=True,
        text=True,
        check=True,
    )
    secrets = yaml.safe_load(result.stdout)

    settings = Settings(
        environment=args.environment,
        app_name=os.getenv("APP_NAME"),
        fake_key=secrets.get("FAKE_KEY", "No FAKE_KEY found in secrets.yaml"),
    )

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("FAKE_KEY: ", settings.FAKE_KEY)
