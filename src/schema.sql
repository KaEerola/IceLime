

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

