import math

class spiral_sort():
    def __init__(self,
                 points=None,
                 rotation=None,
                 start=None,
                 visualize=False):

        self.points = list(set(points))
        self.start = start
        self.visualize = visualize

        self.move = -1 if rotation=="left" else 1

    def sort(self) -> list:
        self.create_spiral()

        if self.visualize:
            self.create_visual()

        return self.sorted_points
            
    def create_spiral(self) -> None:
        match self.start:
            case "N":
                first_point = min(self.points,
                                  key=lambda point: point[1])
                final_points = [(first_point[0]+self.move, first_point[1]),
                                first_point]

            case "S":
                first_point = max(self.points,
                                  key=lambda point: point[1])
                final_points = [(first_point[0]-self.move, first_point[1]),
                                first_point]

            case "W":
                first_point = min(self.points,
                                  key=lambda point: point[0])
                final_points = [(first_point[0], first_point[1]-self.move),
                                first_point]

            case "E":
                first_point = max(self.points,
                                  key=lambda point: point[0])
                final_points = [(first_point[0], first_point[1]+self.move),
                                first_point]

            case _:
                first_point = min(self.points,
                                  key=lambda point: point[1])
                final_points = [(first_point[0], 0),
                                first_point]

        del self.points[self.points.index(first_point)]

        for i in range(len(self.points)):
            angle_point_dict = dict()
            for point in self.points:
                x1, y1 = point
                x2, y2 = final_points[-1]
                x3, y3 = final_points[-2]
                u = (x2-x1, y2-y1)
                v = (x2-x3, y2-y3)

                formula = (u[0]*v[0]+u[1]*v[1])/(math.sqrt(u[0]**2+u[1]**2)*math.sqrt(v[0]**2+v[1]**2))
                angle_point_dict[math.acos(formula)] = point

            selected_angle = angle_point_dict[max(angle_point_dict)]
            final_points.append(selected_angle)
            del self.points[self.points.index(selected_angle)]

        self.sorted_points = final_points[1:]

    def create_visual(self) -> None:
        import tkinter
        width = max(self.sorted_points, key=lambda point: point[0])[0]
        height = max(self.sorted_points, key=lambda point: point[1])[1]

        canvas = tkinter.Canvas(width=width, height=height)
        canvas.pack()

        for point in self.sorted_points:
            canvas.create_oval(point[0]-3,
                               point[1]-3,
                               point[0]+3,
                               point[1]+3,
                               width=0,
                               fill="red")

        canvas.create_line(tuple(self.sorted_points),
                           width=2,
                           fill="green")
