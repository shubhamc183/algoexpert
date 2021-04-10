# Time Complexity: O(NlogN) for quick sort
# Space Complexity: O(1)
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
  redShirtSpeeds.sort(reverse=fastest)
  blueShirtSpeeds.sort()
  solution = 0
  for i in range(len(redShirtSpeeds)):
    solution += max(redShirtSpeeds[i], blueShirtSpeeds[i])
  return solution
