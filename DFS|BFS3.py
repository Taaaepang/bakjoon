from collections import Counter
# 단어변환
def dfs(depth, start, target, words, visited):
    for i in range(len(target)):
        if visited[i] == False:
            if len(Counter(start) - Counter(target[i])) != 1:
                continue
            else:
                visited[i] = True
                if len(Counter(start) - Counter(words)) == 1:
                    return depth
                return dfs(depth + 1, target[i], target, words, visited)


def solution(begin, target, words):
    answer = 0
    visited = [False] * len()
    for i in target:
        if i == words:
            return dfs(1, begin, target, words, visited)
    return 0


def main():
    print(solution("hit", ["hot", "dot", "dog", "lot", "log", "cog"], "cog"))
    print(solution("hit", ["hot", "dot", "dog", "lot", "log"], "cog"))


if __name__ == "__main__":
    main()