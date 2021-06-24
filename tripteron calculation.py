import math

DesiredPoint = [2, 1, 0] #[x y z]


def arm_pos_calc(headpos, arm):

	left_arm_angle_xy = (45/180)*math.pi #radians, 45deg
	left_arm_angle_yz = (1/180)*math.pi #radians, 30deg

	right_arm_angle_xy = (135/180)*math.pi #radians, 135deg
	right_arm_angle_yz = (1/180)*math.pi #radians, 30deg

	middle_arm_angle_xy = (50/180)*math.pi #radians, 50 deg
	middle_arm_angle_yz = (30/180)*math.pi #radians, 30deg

	if arm == "left":
		xp = (1/math.tan(left_arm_angle_xy))*headpos[1]
		xpp = (1/math.tan(left_arm_angle_yz))*headpos[2]
		pos = headpos[0] - xp + xpp

	elif arm == "right":
		xp = (1/math.tan(right_arm_angle_xy))*headpos[1]
		xpp = (1/math.tan(right_arm_angle_yz))*headpos[2]
		pos = headpos[0] - xp + xpp

	else:
		xp = (1/math.tan(middle_arm_angle_xy))*headpos[1]
		xpp = (1/math.tan(middle_arm_angle_yz))*headpos[2]
		pos = headpos[0] - xp + xpp

	print("move the arm to ")
	print(pos)

arm_pos_calc(DesiredPoint, "right")
