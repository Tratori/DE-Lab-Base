# Disclaimer: Created using ChatGPT
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


from helper import *


def plot_join_benchmark():
    df = load_results_benchmark_directory_to_pandas(
        f"{DATA_DIR}/join_benchmark_different_build_sizes"
    )

    unique_ids = df["id"].unique()
    join_algos = df["config.algo"].unique()

    fig, axes = plt.subplots(
        1,
        len(unique_ids),
        figsize=(20, 8),
        sharex=True,
        sharey=True,
    )

    if len(unique_ids) == 1:
        axes = [axes]

    for i, unique_id in enumerate(unique_ids):
        ax = axes[i]
        filtered_df = df[df["id"] == unique_id]

        sns.barplot(
            data=filtered_df,
            x="config.build_size",
            y="runtime",
            hue="config.algo",
            ax=ax,
            zorder=2,
            palette="pastel",
            edgecolor="black",
        )

        ax.set_title(f"{unique_id}")
        ax.set_xlabel("Build Size")
        ax.set_ylabel("Runtime (microseconds)")
        ax.set_yscale("log")
        ax.grid(True, zorder=0, axis="y")
        if i != 0:
            ax.legend([], [], frameon=False)

    handles, labels = axes[0].get_legend_handles_labels()

    plt.tight_layout(rect=[0.0, 0.0, 1, 0.96])
    axes[0].legend(
        handles=handles,
        labels=labels,
        loc="upper center",
        bbox_to_anchor=(len(unique_ids) / 2.0, 1.1),
        ncol=len(join_algos),
        fancybox=True,
        shadow=True,
        fontsize=12,
    )
    # plt.savefig("join_benchmark.png")
    plt.show()


if __name__ == "__main__":
    plot_join_benchmark()
