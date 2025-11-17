import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    import matplotlib.pyplot as plt
    import polars as pl
    import seaborn as sns

    sns.set_style('whitegrid')
    return (pl,)


@app.cell
def _(pl):
    data = pl.read_parquet('data/ad_data.parquet')
    data.group_by([
        'location_state',
        'post_date',
    ]).agg(
        pl.col('url').n_unique()
    ).with_columns(
        location_state = pl.col('location_state').replace({'Rhode-Island': 'Rhode Island'})
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
