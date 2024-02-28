# from xcsoar.mapgen.waypoints.parser import parse_waypoint_file
import Waypoint
import seeyou_reader
from parser_1 import parse_waypoint_file


waypoint_file = open("WaypointFile.cup")
print(f'waypoint_file = {waypoint_file}')
try:
    filename = waypoint_file.name.lower()
    if not filename.endswith(".dat") and (
        filename.endswith(".dat") or not filename.endswith(".cup")
    ):
        raise RuntimeError(
            "Waypoint file {} has an unsupported format.".format(
                waypoint_file.filename
            )
        )
    # desc.bounds = parse_waypoint_file(
    #     waypoint_file.filename, waypoint_file.file
    bounds = parse_waypoint_file(
        waypoint_file.name, waypoint_file
    ).get_bounds()
    print(f'Bounds are {bounds}')
    print(f'filename = {filename}, filename.endswith(".cup") = {filename.endswith(".cup")}')
    waypoint_file = (
        "waypoints.cup" if filename.endswith(".cup") else "waypoints.dat"
    )
    print(f'waypoint_file = {waypoint_file}')
except:
    print("Hit except block")
