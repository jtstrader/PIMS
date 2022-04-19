package com.pims.api.repositories;

import com.pims.api.models.Business;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BusinessRepository extends JpaRepository<Business, Integer>{
}
