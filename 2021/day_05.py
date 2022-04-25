class Thermal:
    
    def __init__(self, input_path = "day_05_sample.py") -> None:
        with open(input_path) as file:
            self.text = file.read().splitlines()
    
    #returns a list with all lines 
    def get_lines(self) -> list:
        points = []
        for item in self.text:
            points.append(item.rsplit(" -> "))
        lines = [{"x_1": int(points[n][0].split(",")[0]), "y_1": int(points[n][0].split(",")[1]), 
            "x_2": int(points[n][1].split(",")[0]), "y_2": int(points[n][1].split(",")[1])} 
            for n in range(0, len(points))]
        return lines
    
    #returns a tuple with the fist item being a list with all horizontal or vertical lines
    #and the second item is a list of all the diagonal lines
    def get_h_v_d_lines(self, lines) -> tuple:
        h_v_lines = [item for item in lines if (item["x_1"]==item["x_2"] or item["y_1"]==item["y_2"])]
        d_lines = [item for item in lines if  (item["x_1"]!=item["x_2"] and item["y_1"]!=item["y_2"]) 
                   and abs(item["x_1"]-item["x_2"]) == abs(item["y_1"]-item["y_2"])] 
        return(h_v_lines, d_lines)
        
    #returns a list with of all the points looking exclusively to the vertical
    #or horizontal lines
    def v_h_points(self, line) -> list:
        points = []
        if line["x_1"] == line["x_2"]:
            if line["y_1"] <= line["y_2"]:
                for number in range(line["y_1"], line["y_2"]+1):
                        points.append((line["x_1"], number))
            else:
                for number in range(line["y_2"], line["y_1"]+1):
                        points.append((line["x_1"], number))
        else:
            if line["x_1"] <= line["x_2"]:
                for number in range(line["x_1"], line["x_2"]+1):
                    points.append((number, line["y_1"]))
            else:
                 for number in range(line["x_2"], line["x_1"]+1):
                    points.append((number, line["y_1"]))
        return points
    
    #returns a list with of all the points looking exclusively to the diagonal lines
    def d_points(self, line):
        points = []
        if line["x_1"] > line["x_2"] and line["y_1"] > line["y_2"]:        
            for item in zip(range(line["x_2"], line["x_1"]+1), range(line["y_2"], line["y_1"]+1)):
                points.append(item)
        elif line['x_1'] > line['x_2'] and line['y_2'] > line['y_1']:
            for item in zip(range(line["x_2"], line["x_1"]+1), range(line["y_2"], line["y_1"]-1,  -1)):
                points.append(item)    
        elif line['x_2'] > line['x_1'] and line['y_1'] > line['y_2']:
            for item in zip(range(line["x_1"], line["x_2"]+1,), range(line["y_1"], line["y_2"]-1,  -1)):
                points.append(item)
        elif line['x_2'] > line['x_1'] and line['y_2'] > line['y_1']:
            for item in zip(range(line["x_1"], line["x_2"]+1), range(line["y_1"], line["y_2"]+1)):
                points.append(item)
        return points
        
    #Shows the number of overlaping points of the horizontal or vertical lines exclusively
    #and also shows the number of overlapping points considering all lines
    def get_overlaping_points(self, h_v_lines, d_lines):
        points = {}
        for item in h_v_lines:
            points_in_line = self.v_h_points(item)
            for point in points_in_line:
                if point in points.keys():
                    points[point] = points[point] + 1
                else:
                    points.update({point: 1})
        print(len({key: value for key, value in points.items() if value !=1}))
        for item in d_lines:
            points_in_diagonal = self.d_points(item)
            for point in points_in_diagonal:
                if point in points.keys():
                    points[point] = points[point] + 1
                else:
                    points.update({point: 1})
        print(len({key: value for key, value in points.items() if value !=1}))

obj = Thermal("day_05_input.txt")
lines = obj.get_lines()
separed_lines = obj.get_h_v_d_lines(lines)
obj.get_overlaping_points(separed_lines[0], separed_lines[1])