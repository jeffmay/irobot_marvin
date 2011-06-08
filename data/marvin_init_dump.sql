PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE PrimativeType (id INTEGER PRIMARY KEY, primative_name TEXT, python_name TEXT);
INSERT INTO "PrimativeType" VALUES(0,'bool','bool');
INSERT INTO "PrimativeType" VALUES(1,'int8','int');
INSERT INTO "PrimativeType" VALUES(2,'uint8','int');
INSERT INTO "PrimativeType" VALUES(3,'int16','int');
INSERT INTO "PrimativeType" VALUES(4,'uint16','int');
INSERT INTO "PrimativeType" VALUES(5,'int32','int');
INSERT INTO "PrimativeType" VALUES(6,'uint32','int');
INSERT INTO "PrimativeType" VALUES(7,'int64','long');
INSERT INTO "PrimativeType" VALUES(8,'uint64','long');
INSERT INTO "PrimativeType" VALUES(9,'float32','float');
INSERT INTO "PrimativeType" VALUES(10,'float64','float');
INSERT INTO "PrimativeType" VALUES(11,'string','string');
INSERT INTO "PrimativeType" VALUES(12,'time','rospy.Time');
INSERT INTO "PrimativeType" VALUES(13,'duration','rospy.Duration');
CREATE TABLE LinkSensationObservation (
    sensation_id INTEGER,
    observation_id INTEGER,
    FOREIGN KEY(sensation_id) REFERENCES Sensation(id),
    FOREIGN KEY(observation_id) REFERENCES Observation(id)
);
CREATE TABLE LinkObservationReaction (
    observation_id INTEGER,
    reaction_id INTEGER,
    FOREIGN KEY(observation_id) REFERENCES Observation(id),
    FOREIGN KEY(reaction_id) REFERENCES Reaction(id)
);
CREATE TABLE Reaction (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    anger REAL,
    confidence REAL,
    excitement REAL,
    fear REAL,
    happiness REAL,
    message TEXT,
    urgency INTEGER
);
CREATE TABLE Observation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT, title TEXT);
CREATE TABLE Sensation (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_name TEXT,
    primative_type_id INTEGER,
    lower_limit REAL,
    upper_limit REAL,
    limit_range REAL,
    int_value INTEGER,
    FOREIGN KEY(primative_type_id) REFERENCES PrimativeType(id)
);
COMMIT;
