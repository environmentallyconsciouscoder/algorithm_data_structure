# class Solution:
#     def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
#         counts = dict(int)
#         left = 0
#         ans = [[], []]
#         for right in range(len(matches)):
#             print("matches", matches)
#             print("won", matches[right][0])
#             print("lose", matches[right][1])

#             counts[matches[right][0]] += 0
#             counts[matches[right][1]] += 1

#         for player, count in counts.items():
#             if count == 0:
#                 ans[0].append(player)
#             elif count == 1:
#                 ans[1].append(player)
#         ans[0].sort()
#         ans[1].sort()
#         return ans

def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    zero_loss = set()
    one_loss = set()
    more_losses = set()

    for winner, loser in matches:
        # Add winner
        if (winner not in one_loss) and (winner not in more_losses):
            zero_loss.add(winner)
        # Add or move loser.
        if loser in zero_loss:
            zero_loss.remove(loser)
            one_loss.add(loser)
        elif loser in one_loss:
            one_loss.remove(loser)
            more_losses.add(loser)
        elif loser in more_losses:
            continue
        else:
            one_loss.add(loser)

    return [sorted(list(zero_loss)), sorted(list(one_loss))]