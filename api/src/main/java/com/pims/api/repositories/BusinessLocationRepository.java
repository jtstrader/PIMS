package com.pims.api.repositories;

import com.pims.api.models.BusinessLocation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface BusinessLocationRepository extends JpaRepository<BusinessLocation, String> {
}
