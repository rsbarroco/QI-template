from pathlib import Path
import typer
from rich.console import Console
from rich.panel import Panel

from qi.prompts import ask
from qi.generator import generate

app = typer.Typer(
    name="qi",
    help="Quality Intelligence — scaffold AI-assisted QA projects.",
    add_completion=False,
)
console = Console()


@app.command()
def main(
    output_dir: Path = typer.Argument(
        None,
        help="Directory to create the project in. Defaults to ./<project-slug>.",
    ),
    dry_run: bool = typer.Option(
        False,
        "--dry-run",
        help="Print what would be generated without writing any files.",
    ),
) -> None:
    console.print(
        Panel.fit(
            "[bold cyan]QI — Quality Intelligence[/bold cyan]\n"
            "Scaffold an AI-assisted QA project in seconds.",
            border_style="cyan",
        )
    )

    config = ask()

    target = output_dir or Path(config.project_slug)

    if dry_run:
        _print_dry_run(config, target)
        return

    generate(config, target)

    console.print(
        Panel.fit(
            f"[bold green]Done![/bold green] Project created at [cyan]{target}[/cyan]\n\n"
            "Next steps:\n"
            f"  cd {target}\n"
            "  git init\n"
            "  # Open in Claude Code and read CLAUDE.md",
            border_style="green",
        )
    )


def _print_dry_run(config, target: Path) -> None:
    from qi.generator import list_files

    console.print(f"\n[bold yellow]Dry run[/bold yellow] — would write to [cyan]{target}/[/cyan]\n")
    for f in list_files(config):
        console.print(f"  [dim]create[/dim]  {f}")
