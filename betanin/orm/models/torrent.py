# betanin
from betanin.status import Status
from betanin.extensions import DB


class Torrent(DB.Model):
    __tablename__ = "torrents"
    id = DB.Column(DB.String, primary_key=True)
    name = DB.Column(DB.String)
    path = DB.Column(DB.String)
    status = DB.Column(DB.Enum(Status))
    created = DB.Column(DB.DateTime, default=DB.func.now())
    updated = DB.Column(
        DB.DateTime, default=DB.func.now(), onupdate=DB.func.now()
    )
    lines = DB.relationship("Line", cascade="all, delete")

    def __str__(self):
        return f"Torrent({self.status})"

    @property
    def has_lines(self):
        return len(self.lines) != 0

    def add_line(self, line):
        line.index = len(self.lines) + 1
        self.lines.append(line)
