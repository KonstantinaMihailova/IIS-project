import pandas as pd
import matplotlib.pyplot as plt


def shorten_query(q):
    mapping = {
        "Where was Alexander the Great born?": "Alexander birth",
        "What language do people speak in North Macedonia?": "Language in N. Macedonia",
        "What is the connection between Cyril and the Slavic alphabet?": "Cyril and Slavic alphabet",
        "What happened at the Battle of Kleidion?": "Battle of Kleidion",
        "What is the UNESCO World Heritage Site near Ohrid?": "UNESCO near Ohrid"
    }
    return mapping.get(q, q[:30])


def main():
    df = pd.read_csv("../output/evaluation.csv")

    df["Short Query"] = df["Query"].apply(shorten_query)

    plt.figure(figsize=(12, 7))

    bars = plt.barh(
        df["Short Query"],
        df["KG Entity Coverage (%)"],
        color="#4f98a3",
        edgecolor="black"
    )

    plt.xlabel("KG Entity Coverage (%)", fontsize=12)
    plt.ylabel("Questions", fontsize=12)
    plt.title("KG-RAG Evaluation Results", fontsize=14, fontweight="bold")
    plt.xlim(0, 100)
    plt.grid(axis="x", linestyle="--", alpha=0.5)

    for bar in bars:
        width = bar.get_width()
        plt.text(
            width + 1,
            bar.get_y() + bar.get_height() / 2,
            f"{width:.1f}%",
            va="center",
            fontsize=10
        )

    plt.tight_layout()
    plt.savefig("../output/evaluation_chart.png", dpi=300, bbox_inches="tight")
    plt.show()

    print("Evaluation chart saved to output/evaluation_chart.png")


if __name__ == "__main__":
    main()