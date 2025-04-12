# instagram-followers-tracker
This Python script uses the Instaloader library to fetch and analyze your Instagram followers and following data. It generates a CSV report showing who you follow, who follows you back, and who doesn't follow you back. Ideal for managing your Instagram account and tracking mutual connections.

## features
- Fetches your **followers** and **following** lists.
- Compares the lists to identify people who **don't follow you back**.
- Generates a **CSV report** for easy data analysis.

### how to use:
1. **install instaloader**:
    ```bash
    pip install instaloader
    ```
2. **clone the repository**:
    ```bash
    git clone https://github.com/adajamile/instagram-followers-tracker.git
    ```
3. **navigate to the project folder**:
    ```bash
    cd instagram-followers-tracker
    ```
4. **run the script**:
    ```bash
    python instagram_followers_tracker.py
    ```
5. **enter your instagram password** when prompted (it will be visible in the terminal, that's how it works).

## output
The script will generate a **CSV file** named `seguidores_relatorio.csv`. This file will contain:
- **Type**: Whether the person follows you back or if you don't follow them back.
- **Username**: The Instagram handle of the person.

If the file already exists, it will generate a new version with a number added to the file name (e.g., `seguidores_relatorio_1.csv`).

## notes
- You may be asked to log in with your Instagram account. If you have **two-factor authentication**, you might need to disable it or use a **session file** to avoid frequent logins.
- If you see the error message "Please wait a few minutes before you try again," simply wait for a while and try again later.

### license
This project is licensed under the MIT License - check out the [LICENSE](LICENSE) file for more details.

