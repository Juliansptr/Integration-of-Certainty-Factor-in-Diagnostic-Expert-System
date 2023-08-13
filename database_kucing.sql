-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 24 Juni 2023 pada 18.38
-- Versi server: 10.1.33-MariaDB
-- Versi PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_cf_flask_kucing`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `gejala`
--

CREATE TABLE `gejala` (
  `id_gejala` varchar(50) NOT NULL DEFAULT '',
  `nama_gejala` varchar(200) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `gejala`
--

INSERT INTO `gejala` (`id_gejala`, `nama_gejala`) VALUES
('1', 'Mengejan dengan melengkungkan tubuhnya'),
('2', 'Gelisah dan mencari tempat untuk buang kotoran'),
('3', 'Sering buang kotoran dan cair'),
('4', 'Adanya kotoran yang menempel di bulu sekitar anus'),
('5', 'Muntah dan terdapat bulu'),
('6', 'Seringkali makan rumput'),
('7', 'Tes sinar UV positif berpendar'),
('8', 'Alopesia atau kebotakan pada kulit'),
('9', 'Terdapat kerak di daerah ujung telinga, siku bagian luar, dada ventral, dan abdomen'),
('10', 'Terlihat banyak tungau di daerah kerokan kucing'),
('11', 'Peradangan pada conjunctiva'),
('12', 'Conjunctiva berwarna merah, bengkak, mungking menutup bola mata dan terlihat jelas'),
('13', 'Keluar leleran purulen pada vulva'),
('14', 'Palpebrae/kelopak mata mengarah ke dalam'),
('15', 'Conjunctiva mata bengkak'),
('16', 'Anus atau rectum keluar'),
('17', 'Muntah berupa makanan, sekret empedu dan terkadang disertai darah'),
('18', 'Nafas menjadi bau'),
('19', 'Sering menggesekkan pantat pada lantai atau tembok'),
('20', 'Keluar cacing berbentuk seperti biji mentimun'),
('21', 'Terdapat luka memar'),
('22', 'Seringkali menjilati daerah yang terluka'),
('23', 'Terlihat kesakitan saat mengeluarkan urine'),
('24', 'Urinasi atau proses mengeluarkan urine tersendat-sendat'),
('25', 'Terlihat daerah ginjal membesar');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('admin', '123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pengetahuan`
--

CREATE TABLE `pengetahuan` (
  `id_pengetahuan` int(50) NOT NULL,
  `id_penyakit` varchar(50) DEFAULT NULL,
  `id_gejala` varchar(50) DEFAULT NULL,
  `mb` double DEFAULT NULL,
  `md` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `pengetahuan`
--

INSERT INTO `pengetahuan` (`id_pengetahuan`, `id_penyakit`, `id_gejala`, `mb`, `md`) VALUES
(1, 'A', '1', 0.9, 0),
(2, 'A', '2', 0.9, 0),
(3, 'B', '3', 0.9, 0),
(4, 'B', '4', 0.9, 0),
(5, 'C', '5', 0.9, 0),
(6, 'C', '6', 0.5, 0),
(7, 'D', '7', 0.9, 0),
(8, 'D', '8', 0.9, 0),
(9, 'E', '9', 0.9, 0),
(10, 'E', '10', 0.9, 0),
(11, 'F', '11', 0.9, 0),
(12, 'F', '12', 0.9, 0),
(13, 'G', '13', 1, 0),
(14, 'H', '14', 0.9, 0),
(15, 'H', '15', 0.9, 0),
(16, 'I', '16', 1, 0),
(17, 'J', '17', 1, 0),
(18, 'K', '18', 1, 0),
(19, 'L', '19', 0.9, 0),
(20, 'L', '20', 0.9, 0),
(21, 'M', '21', 0.9, 0),
(22, 'M', '22', 0.9, 0),
(23, 'N', '23', 0.9, 0),
(24, 'N', '24', 0.9, 0),
(25, 'N', '25', 0.9, 0);

-- --------------------------------------------------------

--
-- Struktur dari tabel `penyakit`
--

CREATE TABLE `penyakit` (
  `id_penyakit` varchar(50) NOT NULL DEFAULT '',
  `nama_penyakit` varchar(200) DEFAULT NULL,
  `solusi_penyakit` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `penyakit`
--

INSERT INTO `penyakit` (`id_penyakit`, `nama_penyakit`, `solusi_penyakit`) VALUES
('A', 'Sembelit', 'Penangan pertama dapat menggunakan larutan enema yang dimasukkan ke dalam dubur. Larutan enema dapat dibuat dari air hangat secukupnya dengan 1/2 sendok teh air sabun, pemberian gliserin 3 cc dan laktulosa. Apabila masih belum membaik segera dibawa ke dokter hewan.'),
('B', 'Diare', 'Injeksi Duradryl 1mg/kgBB, Antibiotik, Dexamethason 0.1 mb/kgBB, dan vitamin ADE.'),
('C', 'Hairbal/Bulu Menggumpal', 'Berikan jus nanas.'),
('D', 'Dermatomycosis', 'Injeksi Duradryl 0.2 cc, ADE 0.1 cc, Griseofulvin 15 mg, 20 hari 1x.'),
('E', 'Skabies', 'Injeksi Ivermectin 0.04 mg/kgBB, Dexamethason 0.2 mb/kgBB, Dipenhidramin 1 mg/kgBB, Vit ADE.'),
('F', 'Conjungtivis', 'Injeksi oksitetrasiklin 7mg/kgBB, Dexamethason 0.1 mg/kgBB, Dipenhidramin 0.2 mg/kgBB.'),
('G', 'Pyomitra', 'Surgery oleh dokter hewan Injeksi sulfadiazin dan trimetropin 15 mg/kgBB, Metronidazole 20 mg/kgBB, Vitamin ADE.'),
('H', 'Entropion', 'Melakukan surgery, sehingga harus dibawa ke dokter hewan.'),
('I', 'Prolap Anus', 'Melakukan surgery, sehingga harus dibawa ke dokter hewan.'),
('J', 'Gastritis', 'Injksi sulfadiazin dan trimetropin 15 mg/kgBB, Ranitidin 5 mg/kgBB (jika tidak berdarah), Neurobion.'),
('K', 'Karang Gigi', 'Dental scaling oleh dokter hewan.'),
('L', 'Dipilidiasis', 'Praziquantel'),
('M', 'Vulnus Traumatika', 'Antiseptik, Amoxicillin 20 mg/kgBB, Gentamisin 4 mg/kgBB, jika luka panjang harus dijahit oleh dokter hewan.'),
('N', 'Feline Urolotiasis Syndrome (FUS)', 'Netfrolit, neurobion, furosemide 4 mg/kgBB, kateterisasi, apabila belum membaik lakukan surgery oleh dokter hewan.');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `gejala`
--
ALTER TABLE `gejala`
  ADD PRIMARY KEY (`id_gejala`);

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- Indeks untuk tabel `pengetahuan`
--
ALTER TABLE `pengetahuan`
  ADD PRIMARY KEY (`id_pengetahuan`);

--
-- Indeks untuk tabel `penyakit`
--
ALTER TABLE `penyakit`
  ADD PRIMARY KEY (`id_penyakit`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `pengetahuan`
--
ALTER TABLE `pengetahuan`
  MODIFY `id_pengetahuan` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
