

CREATE TABLE "inproceedings" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "booktitle" TEXT,
);

CREATE TABLE "books" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "year" integer,
  "publisher" TEXT,
);

CREATE TABLE "articles" (
  "id" SERIAL PRIMARY KEY,
  "author" TEXT,
  "title" TEXT,
  "journal" text,
  "year" integer,
  "volume" integer,
  "pages" TEXT,
);

