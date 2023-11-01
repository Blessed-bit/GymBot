from bd import *
from handlers import *


def calculation_dead(userid):
    dead = show_deadlift(userid)
    return float(dead) / 100 * 80


def calculation_squat(userid):
    squat = show_squat(userid)
    return float(squat) / 100 * 80


def calculation_bench_press(userid):
    bench_press = show_bench_press(userid)
    return float(bench_press) / 100 * 80