import { TestBed } from '@angular/core/testing';

import { CompanyAverageSalaryService } from './company-average-salary.service';

describe('CompanyAverageSalaryService', () => {
  let service: CompanyAverageSalaryService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CompanyAverageSalaryService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
