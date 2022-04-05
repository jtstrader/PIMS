package com.pims.api.repositories;

import com.pims.api.models.Health;
import org.springframework.data.jpa.repository.JpaRepository;

public interface HealthRepository extends JpaRepository<Health, String> {
}
