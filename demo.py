import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    import pathlib
    import socket

    import matplotlib.pyplot as plt
    import polars as pl
    import seaborn as sns

    sns.set_style('whitegrid')
    return pathlib, pl, sns, socket


@app.cell
def _(pathlib, socket):
    dropbox_data_directory_mapper = {
        'nkf-precision-7865': pathlib.Path('/home/nick/Dropbox/git-demo-data/'),
        'nkf-dell-mobile-workstation': pathlib.Path('/home/nick/Dropbox/git-demo-data/'),
    }

    current_hostname = socket.gethostname()
    if current_hostname in dropbox_data_directory_mapper:
        dropbox_data_directory = dropbox_data_directory_mapper.get(current_hostname)
    else:
        print(f' - Host not found in mapper!!!')
    return (dropbox_data_directory,)


@app.cell
def _(dropbox_data_directory, pathlib, pl):
    data_filepath = pathlib.Path(
        dropbox_data_directory,
        'ad_data.parquet',
    )

    data = pl.read_parquet(
        data_filepath
    ).group_by([
        'location_state',
        'post_date',
    ]).agg(
        unique_urls = pl.col('url').n_unique()
    ).with_columns(
        location_state = pl.col('location_state').replace({'Rhode-Island': 'Rhode Island'})
    )
    return (data,)


@app.cell
def _(data, sns):
    sns.lineplot(
        data,
        x='post_date',
        y='unique_urls',
        hue='location_state',
        palette='viridis',
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
