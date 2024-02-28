waypoint_file = Open("WaypointFile.cup")
print(f'waypoint_file.filename =  {waypoint_file.filename}')

if not waypoint_file.file or not waypoint_file.filename:
    print("No waypoint file uploaded.")

try:
    filename = waypoint_file.filename.lower()
    if not filename.endswith(".dat") and (
        filename.endswith(".dat") or not filename.endswith(".cup")
    ):
        raise RuntimeError(
            "Waypoint file {} has an unsupported format.".format(
                waypoint_file.filename
            )
        )
    desc.bounds = parse_waypoint_file(
        waypoint_file.filename, waypoint_file.file
    ).get_bounds()
    desc.waypoint_file = (
        "waypoints.cup" if filename.endswith(".cup") else "waypoints.dat"
    )
except:
    return view.render(
        error="Unsupported waypoint file " + waypoint_file.filename
    ) | HTMLFormFiller(data=params)

        if selection in ["bounds", "waypoint_bounds"]:
            try:
                desc.bounds = GeoRect(
                    float(params["left"]),
                    float(params["right"]),
                    float(params["top"]),
                    float(params["bottom"]),
                )
            except:
                return view.render(error="Map bounds not set.") | HTMLFormFiller(
                    data=params
                )

        if desc.bounds.height() <= 0 or desc.bounds.width() <= 0:
            return view.render(error="Bounds are invalid.") | HTMLFormFiller(
                data=params
            )

        if desc.bounds.height() * desc.bounds.width() > 1000:
            return view.render(error="Selected area is too large.") | HTMLFormFiller(
                data=params
            )

        if self.too_many_requests():
            return view.render(
                error="You can generate only three maps per hour."
            ) | HTMLFormFiller(data=params)

        job = Job(self.__dir_jobs, desc)

        if desc.waypoint_file:
            waypoint_file.file.seek(0)
            f = open(job.file_path(desc.waypoint_file), "w")
            try:
                shutil.copyfileobj(fsrc=waypoint_file.file, fdst=f, length=1024 * 64)
            finally:
                f.close()

        desc.download_url = "/download?uuid=" + job.uuid
        job.enqueue()
        raise cherrypy.HTTPRedirect("/status?uuid=" + job.uuid)

    @cherrypy.expose
    @view.output("status.html")
    def status(self, uuid):
        job = Job.find(self.__dir_jobs, uuid)
        if job is None:
            return view.render("error.html", error="Job not found!")
        status = job.status()
        if status == "Error":
            return view.render("error.html", error="Generation failed!")
        elif status == "Done":
            return view.render("done.html", name=job.description.name, uuid=uuid)
        return view.render(uuid=uuid, name=job.description.name, status=status)

    @cherrypy.expose
    def download(self, uuid):
        job = Job.find(self.__dir_jobs, uuid)
        if not job or job.status() != "Done":
            return self.status(uuid)
        return cherrypy.lib.static.serve_download(
            job.map_file(), job.description.name + ".xcm"
        )
