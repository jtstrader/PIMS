package com.pims.api.repositories;

import com.pims.api.models.Population;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface PopulationRepository extends JpaRepository<Population, String> {
    @Query("SELECT p.ssn, p.first_name, p.last_name FROM Population p")
    public List<String> getPop();
}
