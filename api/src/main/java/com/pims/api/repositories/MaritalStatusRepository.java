package com.pims.api.repositories;

import com.pims.api.models.MaritalStatus;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface MaritalStatusRepository extends JpaRepository<MaritalStatus, String> {
    @Query(nativeQuery = true, value =
            "SELECT l.state, " +
            "SUM(CASE WHEN m.partner_ssn IS NOT NULL THEN 1 ELSE 0 END) AS [Num Married People]" +
            "FROM marital_status m " +
                "JOIN Location l ON (m.ssn = l.ssn) " +
                "JOIN Health h ON (m.ssn = h.ssn)" +
            "WHERE l.state IS NOT NULL AND h.date_of_death IS NOT NULL " +
            "GROUP BY l.state " +
            "ORDER BY [Num Married People] DESC")
    public List<String> getMarriedPeople();
}
