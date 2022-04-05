package com.pims.api.controllers;

import com.pims.api.models.BusinessLocation;
import com.pims.api.repositories.BusinessLocationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api/businessLocation")
public class BusinessLocationController {
    @Autowired
    private BusinessLocationRepository businessLocationRepository;

    @GetMapping
    public List<BusinessLocation> list() { return businessLocationRepository.findAll(); }
}
