def solution(scores):
    result = len(scores)

    paper_best = scores[0][0]
    interview_best = scores[0][1]
    paper_least = scores[0][0]
    interview_least = scores[0][1]

    for paper, interview in scores:
        if paper_best < paper and interview_best < interview:
            result -= 1
            continue

        if paper_least > paper and interview_least > interview:
            result -= 1
            continue

        if paper_best < paper:
            paper_best = paper

        if interview_best < interview:
            interview_best = interview
            
        if paper_least > paper:
            paper_least = paper

        if interview_least > interview:
            interview_least = interview

    print(result)

cases = int(input())
scores = []
for _ in range(cases):
    n = int(input())
    scores.append([])
    for i in range(n):
        document, interview = input().split()
        document, interview = int(document), int(interview)
        scores[-1].append((document, interview))
    
for c in range(cases):
    solution(scores[c])