def del_all_e(s: str, e: str) -> str:
    if not s:
        return ""
    if s[0] == e:
        return del_all_e(s[1:], e)
    return s[0] + del_all_e(s[1:], e)


def main():
    s = input().strip()
    e = input().strip()
    print(del_all_e(s, e))

if __name__ == "__main__":
    main()
