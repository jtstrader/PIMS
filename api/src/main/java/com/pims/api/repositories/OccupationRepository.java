package com.pims.api.repositories;

import com.pims.api.models.Occupation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface OccupationRepository extends JpaRepository<Occupation, String> {
}
