package com.pims.api.repositories;

import com.pims.api.models.Business;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface BusinessRepository extends JpaRepository<Business, Integer>{
    @Query(nativeQuery = true, value = "SELECT  TOP 10 b.name, AVG(o.salary) " +
            "FROM Business b JOIN Occupation o ON (b.business_id = o.business_id) " +
            "GROUP BY o.business_id, b.worth, b.name " +
            "ORDER BY b.worth DESC")
    public List<String> getTop10Salaries();
}
