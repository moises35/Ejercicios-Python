

CREATE TABLE libros (
  id int(11) NOT NULL,
  titulo text NOT NULL,
  autor text NOT NULL,
  estado text NOT NULL
);


ALTER TABLE `libros`
  ADD PRIMARY KEY (`id`);


ALTER TABLE `libros`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

