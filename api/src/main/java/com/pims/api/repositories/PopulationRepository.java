package com.pims.api.repositories;

import com.pims.api.models.Population;
import org.springframework.data.jpa.repository.JpaRepository;

public interface PopulationRepository extends JpaRepository<Population, String> {
}
