package com.pims.api.repositories;

import com.pims.api.models.Occupation;
import org.springframework.data.jpa.repository.JpaRepository;

public interface OccupationRepository extends JpaRepository<Occupation, String> {
}
