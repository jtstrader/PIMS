package com.pims.api.repositories;

import com.pims.api.models.Occupation;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface OccupationRepository extends JpaRepository<Occupation, String> {
    @Query(nativeQuery = true, value =
            "SELECT b.name, o.position, AVG(o.salary) AS [Average Salary] " +
            "FROM Occupation o JOIN Business b ON (o.business_id = b.business_id) " +
            "WHERE o.salary IS NOT NULL " +
            "GROUP BY o.position, b.name " +
            "ORDER BY b.name, [Average Salary] DESC")
    public List<String> averagePositionSalary();
}
