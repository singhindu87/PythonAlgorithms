{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM3wYzpltqooyneRGy+y+ZN",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/singhindu87/PythonAlgorithms/blob/main/Sorts/SelectionSort.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cUvOVa5uWueP",
        "outputId": "b7f86c74-d1b0-46ca-d88a-43566a263e5a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[30, 7, 2, 15, 789, 54]\n",
            "Sorted List\n",
            "[2, 7, 15, 30, 54, 789]\n"
          ]
        }
      ],
      "source": [
        "#Selection Sort\n",
        "# It is comparison-based sorting algorithm\n",
        "# It sorts array by selecting smallest (or largest) element from unsorted portion and swapping it with first unsorted element\n",
        "\n",
        "def selectionsort(arr):\n",
        "  min_idx=0\n",
        "  for i in range(len(arr)):\n",
        "    for j in range(len(arr)-1):\n",
        "      if arr[i]<arr[j]:\n",
        "         (arr[i],arr[j])=(arr[j],arr[i])\n",
        "  return arr\n",
        "\n",
        "mylist=[30,7,2,15,789,54]\n",
        "print(mylist)\n",
        "selectionsort(mylist)\n",
        "print(\"Sorted List\")\n",
        "print(mylist)"
      ]
    }
  ]
}