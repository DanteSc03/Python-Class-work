{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true
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
        "id": "AvYW-sBdkqES"
      },
      "source": [
        "# Exercises using while loops, input function and processing csv files"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**NOTE: Use the commands that we have seen in class up to now.**"
      ],
      "metadata": {
        "id": "8qUP5QXOvoTX"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Write a program that asks by user input deciaml numbers while the user writes greater numbers than the first introduced."
      ],
      "metadata": {
        "id": "wOuICt_UY4ok"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "num1 = float(input(\"Write a decimal number: \"))\n",
        "num2 = float(input(\"Write a decimal number larger than the previous number: \"))\n",
        "while num1 <= num2:\n",
        "  print(\"That's a good choice: \")\n",
        "  num2 = float(input(\"Write a number larger than the previous number: \"))\n",
        "print(\"Unfortunately your number did not meet the criteria :(\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JBwzawIutYrJ",
        "outputId": "443f1872-977c-4b97-e346-32d6478c3564"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Write a decimal number: 1.5\n",
            "Write a decimal number larger than the previous number: 1.6\n",
            "That's a good choice: \n",
            "Write a number larger than the previous number: 1.7\n",
            "That's correct. Way to go!\n",
            "That's a good choice: \n",
            "Write a number larger than the previous number: 1.4\n",
            "That's correct. Way to go!\n",
            "Unfortunately your number did not meet the criteria :(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2. Write a program that calculates the factorial of a certain number introduced using input user. The program will have to check if the number introduced is an integer."
      ],
      "metadata": {
        "id": "qRceVRBuZdw6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "factorial = 1\n",
        "num = int(input(\"Give me a non negative non decimal number to give its factorial:\"))\n",
        "if num%2 != 2 and num >= 0:\n",
        "  for i in range(1,num + 1):\n",
        "       factorial = factorial * i\n",
        "  print(\"The factorial of\",num,\"is\",factorial)\n",
        "else:\n",
        "  print(\"\",num, \"is not an integer\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U45o9pzgvY7y",
        "outputId": "ece46d78-c46c-4f30-faf1-b877c338a851"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Give me a non negative non decimal number to give its factorial:-1\n",
            " -1 was not an integer\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "3. Write a program that reads a sequence of integers ending in 0 and returns the count of even numbers it contains. **Note:** We do not include the final 0. Example:\n",
        "~~~\n",
        "Introduce a number: 3\n",
        "Introduce another number: 6\n",
        "Introduce another number: 2\n",
        "Introduce another number: 0\n",
        "There are 2 even numbers\n",
        "~~~"
      ],
      "metadata": {
        "id": "vSddNwCDvPeu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "count = 0\n",
        "num = int(input(\"Introduce a number: \"))\n",
        "while num != 0:\n",
        "  num = int(input(\"Introduce another number:\"))\n",
        "  if num%2 == 0:\n",
        "    count += 1\n",
        "print(f\"There are {count} even numbers\")\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kFEI55Xoy3Nu",
        "outputId": "1a1f24e9-b971-4398-80d6-d78aedf56ea5"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce a number: 3\n",
            "Introduce another number:6\n",
            "Introduce another number:2\n",
            "Introduce another number:0\n",
            "There are 3 even numbers\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "hICzULS-aPlh"
      },
      "source": [
        "4. Write a program that adds integers as the user enters them via keyboard. The program will stop when the sum exceeds 2000. It should inform the user of the total count of numbers entered, the final sum of the numbers, and the highest and lowest values in the sequence.\n",
        "Example:\n",
        "~~~\n",
        "Introduce a number: 648\n",
        "Introduce another number: 823\n",
        "Introduce another number: 203\n",
        "Introduce another number: 784\n",
        "4 numbers have been introduced, the sum is 2458 and the highest and lowest values are 823 and 203\n",
        "~~~\n",
        "\n",
        "    "
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "nums=[]\n",
        "total_sum=0\n",
        "count=1\n",
        "num = float(input(\"Introduce a number: \"))\n",
        "total_sum = float(num)\n",
        "while total_sum <= 2000:\n",
        "  num = float(input(\"Introduce another number:\"))\n",
        "  nums.append(num)\n",
        "  total_sum+=float(num)\n",
        "  count+=1\n",
        "print(f\"{count-1} numbers have been introduced\")\n",
        "print(f\"The total is {total_sum}\")\n",
        "print(f\"The minimum number is {min(nums)}\")\n",
        "print(f\"The maximum number is {max(nums)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nhNE3bph3Qs-",
        "outputId": "6950ff6d-e0c7-4496-8a2c-500b006bcf3d"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce a number: 648\n",
            "Introduce another number:823\n",
            "Introduce another number:203\n",
            "Introduce another number:784\n",
            "3 numbers have been introduced\n",
            "The total is 2458.0\n",
            "The minimum number is 203.0\n",
            "The maximum number is 823.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "w_NAJtc5aPlb"
      },
      "source": [
        "5. Write a program that reads a sequence of characters that ends in a point ('.'), and tells us how many times the letter 'a' appears without taking care if it is in lower or upper case.\n",
        "Example:  \n",
        "~~~\n",
        "Introduce one character: r\n",
        "Introduce another character: A\n",
        "Introduce another character: t\n",
        "Introduce another character: a\n",
        "Introduce another character: s\n",
        "Introduce another character: .\n",
        "There are 2 'a'\n",
        "~~~\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "letter=[]\n",
        "total_sum=0\n",
        "count=0\n",
        "num = input(\"Introduce one character: \")\n",
        "if letter == \"a\" or letter == \"A\":\n",
        "  count+=1\n",
        "while letter != \".\":\n",
        "  letter = input(\"Introduce another character:\")\n",
        "  if letter == \"a\" or letter == \"A\":\n",
        "    count+=1\n",
        "print(f\"there are {count} 'a' \")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lGmG94Fh7Hh4",
        "outputId": "7db20182-34fc-4338-9e11-2494f30730ca"
      },
      "execution_count": 47,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce one character: r\n",
            "Introduce another character:A\n",
            "Introduce another character:t\n",
            "Introduce another character:a\n",
            "Introduce another character:s\n",
            "Introduce another character:.\n",
            "there are 2 'a' \n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "6. Write a program that reads a sequence of characters ending in '0' and performs a sum according to the following rules:\n",
        "\n",
        "- Lowercase letters are worth 1 point.\n",
        "\n",
        "- Uppercase letters are worth 2 points.\n",
        "\n",
        "- Digits are worth their own numeric value. (For example, '5' is worth 5).\n",
        "\n",
        "- Any other character is worth 0.\n",
        "\n",
        "Example:\n",
        "~~~\n",
        "Introduce one character: a\n",
        "Introduce another character: P\n",
        "Introduce another character: E\n",
        "Introduce another character: ,\n",
        "Introduce another character: 4\n",
        "Introduce another character: 0\n",
        "The sum is 9\n",
        "~~~\n"
      ],
      "metadata": {
        "id": "Q4WtZdNhy2X6"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "alt=[]\n",
        "total_sum=0\n",
        "\n",
        "while alt != '0':\n",
        "  alt = input(\"Introduce another character:\")\n",
        "  if alt.isupper():\n",
        "    total_sum += 2\n",
        "  elif alt.islower():\n",
        "    total_sum += 1\n",
        "  elif alt.isdigit():\n",
        "    total_sum += int(alt)\n",
        "  else:\n",
        "    total_sum += 0\n",
        "\n",
        "print(f\"The total is {total_sum}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XKxB1zTR8COj",
        "outputId": "183aac40-7cf0-40b7-e403-8ab426618009"
      },
      "execution_count": 63,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce another character:a\n",
            "Introduce another character:P\n",
            "Introduce another character:E\n",
            "Introduce another character:,\n",
            "Introduce another character:4\n",
            "Introduce another character:0\n",
            "The total is 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "7. Write a program that reads two integer numbers and admit numbers until one is out of the interval.    \n",
        "Example:\n",
        "~~~\n",
        "Introduce lower value: 3\n",
        "Introduce upper value: 12\n",
        "Introduce a number: 6  \n",
        "Introduce a number: 12  \n",
        "Introduce a number: 10   \n",
        "Introduce a number: 23  \n",
        "The 23 is out of the interval\n",
        "~~~"
      ],
      "metadata": {
        "id": "Iwt76UKLzlyR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "low = int(input(\"Introduce a lower value: \"))\n",
        "upper = int(input(\"Introduce a upper value: \"))\n",
        "num = int(input(\"Introduce a number:\"))\n",
        "\n",
        "\n",
        "while low <= num <= upper:\n",
        "  num = int(input(\"Introduce a number:\"))\n",
        "\n",
        "print(f\"The {num} is out of the interval\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ujRvY4gD_qRg",
        "outputId": "67843a1b-bf3d-48ef-f172-9f1bb53a64fe"
      },
      "execution_count": 69,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Introduce a lower value: 3\n",
            "Introduce a upper value: 12\n",
            "Introduce a number:6\n",
            "Introduce a number:12\n",
            "Introduce a number:10\n",
            "Introduce a number:23\n",
            "The 23 is out of the interval\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "8. Using the file 'PPR-2015.csv', write a program that calculates the average price of the houses sold in January (the year is alwyas 2015)."
      ],
      "metadata": {
        "id": "KgMdHAofaZqB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yM4a9xncBA1m",
        "outputId": "b8a23b5b-f235-4d53-fbea-7c9f158ff288"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%cd /content/drive/MyDrive/Colab\\ Notebooks/\n",
        "!ls"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "U4vvrb82BLu2",
        "outputId": "a3ae470b-fee5-4aee-bb58-1b3a7c7e86bd"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/Colab Notebooks\n",
            " 01_Hello_Python_ProgII_24.ipynb\t       Exercises_03_while_loop_24.ipynb\n",
            " 02_Lists_ProgII_24.ipynb\t\t       PPR-2015.csv\n",
            "'03_while_loop_input_csv_ProgII_24(1).ipynb'   Schrantz_Dante.ipynb\n",
            " Exercises_02_Lists.ipynb\t\t       Untitled0.ipynb\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import csv\n",
        "csv_path = \"PPR-2015.csv\"\n",
        "n_rows=5\n",
        "\n",
        "with open(csv_path,\"r\") as file:\n",
        "  reader = csv.reader(file)\n",
        "  for n, row in enumerate(reader):\n",
        "    print(row)\n",
        "    if n==n_rows:\n",
        "      break"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jHaOSnQ7J3Ih",
        "outputId": "94d6124c-ee9b-44b4-8451-230a9501e21f"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['Date of Sale (dd/mm/yyyy)', 'Address', 'Postal Code', 'County', 'Price (€)', 'Not Full Market Price', 'VAT Exclusive', 'Description of Property', 'Property Size Description']\n",
            "['02/01/2015', '108 THE HARDWICKE VILLAGE, NORTH BRUNSWICK ST, DUBLIN 7', 'Dublin 7', 'Dublin', '€138,000.00', 'No', 'No', 'Second-Hand Dwelling house /Apartment', '']\n",
            "['02/01/2015', '12 THE CEDARS, MONKSTOWN VALLEY, MONKSTOWN', '', 'Dublin', '€270,000.00', 'No', 'No', 'Second-Hand Dwelling house /Apartment', '']\n",
            "['02/01/2015', '148 DEEL MANOR, ASKEATON, CO LIMERICK', '', 'Limerick', '€67,000.00', 'No', 'No', 'Second-Hand Dwelling house /Apartment', '']\n",
            "['02/01/2015', '4 SHREWSBURY, BALLSBRIDGE, DUBLIN 4', 'Dublin 4', 'Dublin', '€900,000.00', 'No', 'No', 'Second-Hand Dwelling house /Apartment', '']\n",
            "['02/01/2015', '41 THE BRIARY, BLAINROE, WICKLOW', '', 'Wicklow', '€176,000.00', 'Yes', 'No', 'Second-Hand Dwelling house /Apartment', '']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import csv\n",
        "csv_path = \"PPR-2015.csv\"\n",
        "n_rows=5\n",
        "list_h=[]\n",
        "l_prices=[]\n",
        "num_col=4\n",
        "\n",
        "with open(csv_path, \"r\") as file:\n",
        "    reader = csv.reader(file)\n",
        "    for n, row in enumerate(reader):\n",
        "        list_h.append(row)\n",
        "\n",
        "for row in range(1, len(list_h)):\n",
        "    price=list_h[row][num_col]\n",
        "    price=price.split('.')\n",
        "    price=price[0]\n",
        "    l_prices.append(int(price[1:].replace(',', '')))\n",
        "\n",
        "av_price= sum(l_prices)/len(l_prices)\n",
        "print(f\"The average price of the houses is {av_price:.2f} euros\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BsFadgbGBNCU",
        "outputId": "90a5d5f6-42e2-4313-8c20-5e6d9403fdf2"
      },
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The average price of the houses is 220165.36 euros\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "9. Using the file 'PPR-2015.csv', write a program that calculates how many different postal codes there are in the file and print them."
      ],
      "metadata": {
        "id": "8xZRuNiYbWwi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import csv\n",
        "csv_path = \"PPR-2015.csv\"\n",
        "n_rows=5\n",
        "list_h=[]\n",
        "num_col=2\n",
        "postal_codes=0\n",
        "unique_postal_codes = set()\n",
        "\n",
        "with open(csv_path, \"r\") as file:\n",
        "    reader = csv.reader(file)\n",
        "    next(reader)\n",
        "    for row in reader:\n",
        "        if len(row) > num_col:\n",
        "            postal_code = row[num_col].strip()\n",
        "            unique_postal_codes.add(postal_code)\n",
        "\n",
        "num_unique_postal_codes = len(unique_postal_codes)\n",
        "print(f\"The number of unique postal codes are {num_unique_postal_codes} and are the following {unique_postal_codes}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JANxakIxIUVH",
        "outputId": "c6cc7f31-54a1-423a-fb0c-2ea7e9e7dcae"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The number of unique postal codes are 24 and are the following {'', 'Dublin 12', 'Dublin 1', 'Dublin 10', 'Dublin 11', 'Dublin 5', 'Dublin 6', 'Dublin 22', 'Dublin 20', 'Dublin 18', 'Ní Bhaineann', 'Dublin 4', 'Dublin 17', 'Dublin 8', 'Dublin 24', 'Dublin 9', 'Dublin 6w', 'Dublin 14', 'Dublin 15', 'Dublin 7', 'Dublin 2', 'Dublin 3', 'Dublin 16', 'Dublin 13'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "10. Using the file 'PPR-2015.csv', write a program that calculates the average price of the houses sold in the different postal codes and print them both."
      ],
      "metadata": {
        "id": "DH88Tovbb5aX"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1IZjiAkyOODO",
        "outputId": "6d245cba-9a87-4d14-d21a-726e5e527f55"
      },
      "execution_count": 50,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Average Prices of Houses Sold in Different Postal Codes:\n"
          ]
        }
      ]
    }
  ]
}