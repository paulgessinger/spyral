import typer


app = typer.Typer()

@app.command()
def main():
    print("hi")

