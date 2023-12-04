class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        short = 0
        short2 = 0
        total = sum(distance)
        if start <= destination:
            short = sum(distance[start : destination])
            short2 = total - short
        else:
            short = sum(distance[destination : start])
            short2 = total - short
        return min(short , short2)

      