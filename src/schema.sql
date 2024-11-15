CREATE TABLE "references" (
  "id" SERIAL PRIMARY KEY,
  "name" TEXT UNIQUE
);

CREATE TABLE "inproceedings" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "booktitle" TEXT,
  "reference_id" INTEGER
);

CREATE TABLE "books" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "publisher" TEXT,
  "reference_id" INTEGER
);

CREATE TABLE "articles" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "journal" text,
  "year" integer,
  "volume" integer,
  "pages" TEXT,
  "reference_id" INTEGER
);

ALTER TABLE "books" ADD FOREIGN KEY ("reference_id") REFERENCES "references" ("id") ON DELETE CASCADE;

ALTER TABLE "articles" ADD FOREIGN KEY ("reference_id") REFERENCES "references" ("id") ON DELETE CASCADE;

ALTER TABLE "inproceedings" ADD FOREIGN KEY ("reference_id") REFERENCES "references" ("id") ON DELETE CASCADE;
