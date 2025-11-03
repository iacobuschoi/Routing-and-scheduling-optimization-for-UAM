import math

def path_to_posvec(path, t_departure: float, delta_t: float = 0.1, v: float = 10.0):
    
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

    pos_vec = []

    seg_idx = 0     # segment index
    seg_trav = 0.0  # 이번 segment에서 이동한 거리
    x0, y0, x1, y1, seg_len, ux, uy = segs[seg_idx]

    # k = 0 … N (시작과 마지막 포함)
    for k in range(N + 1):
        t_k = round(t_departure + k * delta_t, 9)
        s_target = v * k * delta_t
        if s_target >= total_len - 1e-12:
            # 마지막 node
            x_end = segs[-1][2]
            y_end = segs[-1][3]
            pos_vec.append((t_k, float(x_end), float(y_end)))
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

        pos_vec.append((t_k, float(x), float(y)))

    return pos_vec


# if __name__ == "__main__":
#     # class Node:
#     #     def __init__(self, id, pos_x, pos_y):
#     #         self.id = id
#     #         self.pos = [pos_x, pos_y]

#     n0 = Node(0, 0.000, 0.000)
#     n1 = Node(1, 0.000, 10.000)
#     n2 = Node(2, 10.000, 0.000)
#     n3 = Node(3, 10.000, 20.000)
#     path = [n0, n1, n2, n3]

#     pos_vec = path_to_posvec(path, 0.0)
    
    # for t, x, y in pos_vec:
    #     print(f"t={t:.2f}, x={x:.2f}, y={y:.2f}")