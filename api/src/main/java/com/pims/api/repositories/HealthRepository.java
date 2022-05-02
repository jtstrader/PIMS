package com.pims.api.repositories;

import com.pims.api.models.Health;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface HealthRepository extends JpaRepository<Health, String> {
    @Query(nativeQuery = true, value = "SELECT l.state," +
            "(SUM(CASE WHEN h.date_of_death IS NOT NULL THEN 1.0 ELSE 0.0 END) / SUM(CASE WHEN h.date_of_death IS NULL THEN 1.0 ELSE 0.0 END)) " +
            "AS [Average Death Rate]" +
            "FROM Health h JOIN Location l ON (h.ssn = l.ssn) " +
            "WHERE l.state IS NOT NULL " +
            "GROUP BY l.state " +
            "ORDER BY [Average Death Rate] DESC")
    public List<String> getAvgDeathRate();

    @Query(nativeQuery = true, value= "SELECT " +
            "SUM(CASE WHEN h.date_of_Death IS NULL THEN 1.0 ELSE 0.0 END) AS [people alive], " +
            "SUM(CASE WHEN h.date_of_Death IS NOT NULL THEN 1.0 ELSE 0.0 END) AS [people dead]" +
            "FROM Health h")
    public List<String> getDeathRatio();
}
