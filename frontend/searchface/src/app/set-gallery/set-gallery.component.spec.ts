import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SetGalleryComponent } from './set-gallery.component';

describe('SetGalleryComponent', () => {
  let component: SetGalleryComponent;
  let fixture: ComponentFixture<SetGalleryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SetGalleryComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SetGalleryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
