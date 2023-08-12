days=int(input())
year=days//365
day=days-(year*365)
weeks=day//7
print(f"{year}")
print(f"{weeks}")