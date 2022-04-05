package com.pims.api.controllers;

import com.pims.api.models.Health;
import com.pims.api.repositories.HealthRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/health")
public class HealthController {
    @Autowired
    private HealthRepository healthRepository;

    @GetMapping
    public List<Health> list() { return healthRepository.findAll(); }
}
