import math

# class ActiveFlightRoute():
#     def __init__(self):
#         self.positionVectorList = []
    
#     def append_pv(self, pv):
#         self.positionVectorList.append(pv)

class PositionVector():
    def __init__(self, t_departure, path):
        self.initTime = t_departure
        self.arrivedTime, self.vector = self.path_to_posvec(path, t_departure)
    
    def path_to_posvec(self, path, t_initial: float, delta_t: float = 0.1, v: float = 10.0):
    
        segs = []   # (x0, y0, x1, y1, seg_len, ux, uy)
        total_len = 0.0

        for i in range(len(path) - 1):
            x0, y0 = path[i].pos[0], path[i].pos[1]
            x1, y1 = path[i + 1].pos[0], path[i + 1].pos[1]
            dx, dy = x1 - x0, y1 - y0
            seg_len = math.hypot(dx, dy)
            if seg_len < 1e-12:
                continue
            ux, uy = dx / seg_len, dy / seg_len
            segs.append((x0, y0, x1, y1, seg_len, ux, uy))
            total_len += seg_len

        total_time = total_len / v
        N = math.ceil(total_time / delta_t)     # sample 개수, 마지막 node 포함하도록 ceil
        t_final = t_initial + N * delta_t

        pos_vec = []

        seg_idx = 0     # segment index
        seg_trav = 0.0  # 이번 segment에서 이동한 거리
        x0, y0, x1, y1, seg_len, ux, uy = segs[seg_idx]

        # k = 0 … N (시작과 마지막 포함)
        for k in range(N + 1):
            s_target = v * k * delta_t
            if s_target >= total_len - 1e-12:
                # 마지막 node
                x_end = segs[-1][2]
                y_end = segs[-1][3]
                pos_vec.append([float(x_end), float(y_end)])
                continue

            cum = 0.0       # 누적거리
            for j in range(seg_idx):
                cum += segs[j][4]
            cum += seg_trav

            need = s_target - cum  # 앞으로 더 가야하는 거리 (>= 0이어야 정상)

            if need < -1e-9:    # 부동소수점 오류 -> 다시 계산
                seg_idx = 0
                seg_trav = 0.0
                x0, y0, x1, y1, seg_len, ux, uy = segs[seg_idx]
                need = s_target

            while need > (seg_len - seg_trav) - 1e-12:
                need -= (seg_len - seg_trav)
                seg_idx += 1
                seg_trav = 0.0
                x0, y0, x1, y1, seg_len, ux, uy = segs[seg_idx]

            seg_trav += max(0.0, need)
            x = x0 + ux * seg_trav
            y = y0 + uy * seg_trav

            pos_vec.append([float(x), float(y)])

        return t_final, pos_vec
    
    def collision_detect(self, otherPositionVector, minDist = 5, delta_t: float = 0.1):
        
        def _dist(p, q):
            return math.hypot(p[0] - q[0], p[1] - q[1])
        
        # 겹치는 구간
        t_start = max(self.initTime, otherPositionVector.initTime)
        t_end = min(self.arrivedTime, otherPositionVector.arrivedTime)
        
        # 겹치는 구간이 없을 경우 -> False
        if t_start > t_end:
            return False
        
        # 시작 인덱스
        k_self = int(round((t_start - self.initTime) / delta_t))
        k_other = int(round((t_start - otherPositionVector.initTime) / delta_t))
        
        steps = int(math.floor((t_end - t_start) / delta_t)) + 1
        
        for s in range(steps):
            if _dist(self.vector[k_self + s], otherPositionVector.vector[k_other + s]) <= minDist:
                # 디버깅용
                # print(self.vector[k_self + s], otherPositionVector.vector[k_other + s])
                return True
        
        return False
        
    
    def collision_detect_with_activate(self, ActiveFlightRoute):
        if ActiveFlightRoute.positionVectorList is None:
            return False
        
        for positionVector in ActiveFlightRoute.positionVectorList:
            if self.collision_detect(positionVector):
                return True
        
        return False