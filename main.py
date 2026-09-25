import requests
from lib import calculate_discount, format_status_message


def main() -> None:
    user_info = format_status_message("alex_dev", "administrator")
    final_price = calculate_discount(1500.0, 15.0)

    print(user_info)
    print(f"Discounted price: {final_price:.2f}")

    response = requests.get("https://api.github.com")
    print(f"GitHub API status code: {response.status_code}")


if __name__ == "__main__":
    main()
    print("App updated successfully in feature branch!")