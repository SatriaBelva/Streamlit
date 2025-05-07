CREATE TABLE `kecamatan` (
  `KecamatanID` int NOT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `RT_miskin` int DEFAULT NULL,
  `indeks_ekonomi` int DEFAULT NULL,
  `indeks_ekonomi_normalized` int DEFAULT NULL,
  `tingkat_ekonomi` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `kelurahan` (
  `KelurahanID` int NOT NULL,
  `KecamatanID` int DEFAULT NULL,
  `nama` varchar(255) DEFAULT NULL,
  `jumlah_KK` int DEFAULT NULL,
  `jumlah_penduduk` int DEFAULT NULL,
  `laki_laki` int DEFAULT NULL,
  `perempuan` int DEFAULT NULL,
  `tidakbelum_sekolah` int DEFAULT NULL,
  `belum_tamatSD` int DEFAULT NULL,
  `tamatSD` int DEFAULT NULL,
  `SLTP` int DEFAULT NULL,
  `SLTA` int DEFAULT NULL,
  `D1_D2` int DEFAULT NULL,
  `D3` int DEFAULT NULL,
  `S1` int DEFAULT NULL,
  `S2` int DEFAULT NULL,
  `S3` int DEFAULT NULL,
  `belumtidak_kerja` int DEFAULT NULL,
  `nelayan` int DEFAULT NULL,
  `pelajar_mahasiswa` int DEFAULT NULL,
  `pensiunan` int DEFAULT NULL,
  `perdagangan` int DEFAULT NULL,
  `IRT` int DEFAULT NULL,
  `wiraswasta` int DEFAULT NULL,
  `guru` int DEFAULT NULL,
  `perawat` int DEFAULT NULL,
  `pengacara` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `user` (
  `UserID` int NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE `kecamatan`
  ADD PRIMARY KEY (`KecamatanID`);

ALTER TABLE `kelurahan`
  ADD PRIMARY KEY (`KelurahanID`),
  ADD KEY `KecamatanID` (`KecamatanID`);

ALTER TABLE `user`
  ADD PRIMARY KEY (`UserID`);

ALTER TABLE `kelurahan`
  ADD CONSTRAINT `kelurahan_ibfk_1` FOREIGN KEY (`KecamatanID`) REFERENCES `kecamatan` (`KecamatanID`);
COMMIT;

INSERT INTO `kelurahan` (`KelurahanID`, `KecamatanID`, `nama`, `jumlah_KK`, `jumlah_penduduk`, `laki_laki`, `perempuan`, `tidakbelum_sekolah`, `belum_tamatSD`, `tamatSD`, `SLTP`, `SLTA`, `D1_D2`, `D3`, `S1`, `S2`, `S3`, `belumtidak_kerja`, `nelayan`, `pelajar_mahasiswa`, `pensiunan`, `perdagangan`, `IRT`, `wiraswasta`, `guru`, `perawat`, `pengacara`) VALUES
(1, 16, 'PADOMASAN', 4031, 10848, 5413, 5435, 2455, 1474, 3266, 1815, 1548, 39, 37, 207, 7, 0, 2585, 5, 1167, 32, 64, 1870, 2538, 89, 6, 0),

INSERT INTO `kecamatan` (`KecamatanID`, `nama`, `RT_miskin`, `indeks_ekonomi`, `indeks_ekonomi_normalized`, `tingkat_ekonomi`) VALUES
(1, 'Kencong', 62830, 1, 96, 'Tinggi'),

INSERT INTO `user` (`UserID`, `email`, `password`) VALUES
(1, 'internshiprlo@gmail.com', 'intern12345');