package com.pims.api.repositories;

import com.pims.api.models.MaritalStatus;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MaritalStatusRepository extends JpaRepository<MaritalStatus, String> {
}
