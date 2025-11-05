import requests


def main():
    msg = "Salom, bu mening xabarim"
    webhook_url = "https://webhook.site/0dd410b9-b987-44e8-9d96-3b7eaa0187b2"

    post_payload = {"msg": msg, "url": webhook_url}

    print("1) POST so'rov yuborilyapti...")
    try:
        post_resp = requests.post("https://test.icorp.uz/interview.php", json=post_payload, timeout=15)
        post_resp.raise_for_status()
    except Exception as e:
        print("POST so'rovda xato:", e)
        return

    first_code = post_resp.json().get("part1", "")
    print("1-qism kodi (serverdan):", first_code)
    print(
        "\nEndi webhook (webhook.site yoki shunga o'xshash) sahifasiga o'tib, API tomonidan yuborilgan 2-qism kodni oling.")
    print("Masalan: https://webhook.site/ sahifasiga kiring va so'rovni tekshiring.")

    second_code = input("\nWebhook'dan olingan 2-qism kodni kiriting: ").strip()
    if not second_code:
        print("2-qism kod kiritilmadi. Dastur tugadi.")
        return

    full_code = first_code + second_code
    print("\nBirlashtirilgan kod:", full_code)

    get_url = f"https://test.icorp.uz/interview.php?code={full_code}"
    print("GET so'rov yuborilyapti...")
    try:
        get_resp = requests.get(get_url, timeout=15)
        get_resp.raise_for_status()
    except Exception as e:
        print("GET so'rovda xato:", e)
        return

    final_message = get_resp.text.strip()
    print("\n=== NATIJA ===")
    print("Birlashtirilgan kod:", full_code)
    print("Asl xabar:", final_message)


if __name__ == "__main__":
    main()

